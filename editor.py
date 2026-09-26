import sys
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def make_magic_video(input_video_path, output_video_path):
    print("ভিডিও প্রসেস করা হচ্ছে...")
    clip = VideoFileClip(input_video_path)
    short_clip = clip.subclip(0, min(10, clip.duration))
    fast_clip = short_clip.speedx(1.5)
    
    txt_clip = TextClip("AI Magic Edit", fontsize=50, color='white', font='Arial-Bold')
    txt_clip = txt_clip.set_pos('center').set_duration(fast_clip.duration)
    
    final_video = CompositeVideoClip([fast_clip, txt_clip])
    final_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
    print("ম্যাজিক ভিডিও তৈরি সম্পন্ন!")

if __name__ == "__main__":
    make_magic_video("input.mp4", "output_magic.mp4")
