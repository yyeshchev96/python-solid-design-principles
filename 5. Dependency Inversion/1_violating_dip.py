"""
Dependency Inversion: high-level modules should depend on abstractions rather than concrete implementations

In other words: 
- avoid multiple inheritance
- rely on stable abstractions
- don't refer to volatile concrete classes - refer to abstract interfaces instead
"""

from abc import ABC, abstractmethod


# GIVEN we have the following structure
class BaseMediaEncoder(ABC):
    pass


class VideoMediaEncoder(BaseMediaEncoder):
    pass


class MP4MediaEncoder(VideoMediaEncoder):
    pass


# Here we have 3 levels of classes:
#   MP4MediaEncoder -> VideoMediaEncoder -> BaseMediaEncoder
