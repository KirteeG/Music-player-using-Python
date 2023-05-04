#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Import liberaries

import os
import pygame
import tkinter as tk
from tkinter import ttk

# initialize pygame mixer

pygame.mixer.init()


# In[27]:


# create GUI window

root = tk.Tk()
root.title("Music Player")


# In[21]:


# create label for song name

song_label = ttk.Label(root, text="Song Name")
song_label.pack()


# In[22]:


# define music playlist

playlist = [r"C:\Users\Dell\Desktop\New project by k\Pandas\life-is-beautiful-110057.mp3", r"C:\Users\Dell\Desktop\New project by k\Pandas\sunset by the sea.mp3"]
current_song_index = 0


# In[23]:


# define functions for player controls

def play():
    global current_song_index
    # get the name of the currently playing song
    song_path = playlist[current_song_index]
    song_name = os.path.basename(song_path)
    # update the song label with the name of the currently playing song
    song_label.config(text=song_name)
    # load and play the currently playing song
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def stop():
    global current_song_index
    pygame.mixer.music.stop()
    current_song_index = 0

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    play()


# In[24]:


# create control buttons

play_button = ttk.Button(root, text="Play", command=play)
play_button.pack()

pause_button = ttk.Button(root, text="Pause", command=pause)
pause_button.pack()

unpause_button = ttk.Button(root, text="Unpause", command=unpause)
unpause_button.pack()

stop_button = ttk.Button(root, text="Stop", command=stop)
stop_button.pack()

next_button = ttk.Button(root, text="Next", command=next_song)
next_button.pack()

prev_button = ttk.Button(root, text="Previous", command=prev_song)
prev_button.pack()


# In[25]:


# create volume slider

volume_label = ttk.Label(root, text="Volume")
volume_label.pack()
volume_slider = ttk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, command=lambda x: pygame.mixer.music.set_volume(float(x)))
volume_slider.pack()


# In[26]:


# start GUI loop
root.mainloop()

