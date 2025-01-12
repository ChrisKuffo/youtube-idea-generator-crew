import os
from typing import Dict, List, Type

import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Define a model for video search results with necessary fields
class VideoSearchResult(BaseModel):
    video_id: str
    title: str
    channel_id: str
    channel_title: str
    days_since_published: int

# Define a model for video details with necessary fields
class VideoDetails(BaseModel):
    title: str
    view_count: int
    url: str

# Define input schema for the tool using Pydantic BaseModel
class YoutubeVideoSearchAndDetailsToolInput(BaseModel):
    keyword: str = Field(..., description="The search keyword.")
    max_results: int = Field(3, description="The maximum number of results to return.")

# Main class for the YouTube video search and details tool
class YoutubeVideoSearchAndDetailsTool(BaseTool):
    # Tool name and description
    name: str = "Search YouTube Videos"
    description: str = (
        "Searches YouTube videos based on a keyword and retrieves details for each video."
    )
    # Define the schema for the tool's arguments
    args_schema: Type[BaseModel] = YoutubeVideoSearchAndDetailsToolInput
    # Retrieve the API key from environment variables
    api_key: str = Field(default_factory=lambda: os.getenv("YOUTUBE_API_KEY"))

    # Method to fetch video details synchronously
    def fetch_video_details_sync(self, video_id: str) -> VideoDetails:
        # YouTube API endpoint for video details
        url = "https://www.googleapis.com/youtube/v3/videos"
        # Parameters for the API request
        params = {"part": "snippet,statistics", "id": video_id, "key": self.api_key}
        # Make the API request
        response = requests.get(url, params=params)
        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        # Extract the first item from the response
        item = response.json().get("items", [])[0]
        # Extract necessary details from the response
        title = item["snippet"]["title"]
        view_count = int(item["statistics"]["viewCount"])
        video_url = f"https://youtube.com/watch?v={video_id}"
        # Return the video details as a VideoDetails object
        return VideoDetails(title=title, view_count=view_count, url=video_url)

    # Method to run the tool and fetch video details
    def _run(self, keyword: str, max_results: int = 3) -> List[Dict]:
        # YouTube API endpoint for searching videos
        url = "https://www.googleapis.com/youtube/v3/search"
        # Parameters for the API request
        params = {
            "part": "snippet",
            "q": keyword,
            "maxResults": max_results,
            "type": "video",
            "key": self.api_key,
        }
        # Make the API request
        response = requests.get(url, params=params)
        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        # Extract items from the response
        items = response.json().get("items", [])

        # Fetch details for each video and return as a list of dictionaries
        video_details = [
            self.fetch_video_details_sync(item["id"]["videoId"]) for item in items
        ]
        return [video.model_dump() for video in video_details]