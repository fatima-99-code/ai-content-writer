"""
content_generator.py

Handles content generation logic.

Currently uses a placeholder (template-based) generator so the app
works out of the box without any API key.

To connect your own AI provider (e.g., OpenAI, Anthropic, Gemini):
1. Add your API key (use st.secrets or environment variables — never hardcode it).
2. Replace the body of `generate_content()` with a call to your AI provider's API.
3. Keep the function signature the same: generate_content(topic, content_type) -> str
"""

import random


def generate_content(topic: str, content_type: str) -> str:
    """
    Generate content based on the given topic and content type.

    Args:
        topic: The subject/topic provided by the user.
        content_type: One of "Blog Post", "Instagram Caption",
                       "LinkedIn Post", "Product Description".

    Returns:
        A string containing the generated content.
    """
    generators = {
        "Blog Post": _generate_blog_post,
        "Instagram Caption": _generate_instagram_caption,
        "LinkedIn Post": _generate_linkedin_post,
        "Product Description": _generate_product_description,
    }

    generator_fn = generators.get(content_type, _generate_blog_post)
    return generator_fn(topic)


# ----------------------------
# Placeholder Generators
# ----------------------------

def _generate_blog_post(topic: str) -> str:
    return (
        f"# {topic.title()}\n\n"
        f"## Introduction\n"
        f"In today's fast-paced world, understanding **{topic}** has become more "
        f"important than ever. This post explores the key aspects, benefits, "
        f"and practical tips related to {topic}.\n\n"
        f"## Why It Matters\n"
        f"{topic.title()} affects many areas of our daily lives. By diving deeper "
        f"into this subject, readers can gain valuable insights that lead to "
        f"better decisions and outcomes.\n\n"
        f"## Key Takeaways\n"
        f"- A clear overview of {topic}\n"
        f"- Practical tips you can apply today\n"
        f"- Common mistakes to avoid\n\n"
        f"## Conclusion\n"
        f"To sum up, {topic} is a topic worth paying attention to. Start applying "
        f"these insights today and see the difference for yourself.\n\n"
        f"*(This is placeholder content. Connect your AI API in content_generator.py "
        f"to generate real, dynamic blog posts.)*"
    )


def _generate_instagram_caption(topic: str) -> str:
    emojis = ["✨", "🔥", "💡", "🌿", "🚀", "💪", "🌟"]
    hashtags = " ".join(
        f"#{word.lower()}" for word in topic.split() if word.isalpha()
    )
    return (
        f"{random.choice(emojis)} Let's talk about {topic}! {random.choice(emojis)}\n\n"
        f"Here's why it deserves a spot in your daily routine — small changes, "
        f"big impact. 💯\n\n"
        f"👉 Double-tap if you agree!\n"
        f"💬 Drop a comment with your thoughts.\n\n"
        f"{hashtags} #motivation #dailyinspo\n\n"
        f"_(Placeholder caption — connect your AI API for personalized captions.)_"
    )


def _generate_linkedin_post(topic: str) -> str:
    return (
        f"Thoughts on {topic} 💼\n\n"
        f"Over the past few months, I've been exploring {topic} and its impact "
        f"on the industry. Here are a few insights I'd like to share:\n\n"
        f"1️⃣ It's reshaping how professionals approach their work.\n"
        f"2️⃣ Early adopters are already seeing measurable benefits.\n"
        f"3️⃣ The learning curve is smaller than most people expect.\n\n"
        f"If you're not already exploring {topic}, now might be a great time "
        f"to start.\n\n"
        f"What's your experience with {topic}? Let's discuss in the comments. 👇\n\n"
        f"#{topic.split()[0].lower() if topic.split() else 'business'} "
        f"#professionaldevelopment #growth\n\n"
        f"(Placeholder post — connect your AI API in content_generator.py for "
        f"tailored LinkedIn content.)"
    )


def _generate_product_description(topic: str) -> str:
    return (
        f"**{topic.title()}**\n\n"
        f"Discover the perfect solution with our {topic}. Designed with quality "
        f"and performance in mind, this product is built to exceed your "
        f"expectations.\n\n"
        f"**Key Features:**\n"
        f"- Premium quality materials\n"
        f"- Designed for everyday use\n"
        f"- Reliable performance you can trust\n"
        f"- Sleek, modern design\n\n"
        f"**Why Choose This Product?**\n"
        f"Whether you're looking for convenience, durability, or style, our "
        f"{topic} delivers on all fronts. Customers consistently praise its "
        f"value and performance.\n\n"
        f"Order now and experience the difference for yourself!\n\n"
        f"*(Placeholder description — connect your AI API in content_generator.py "
        f"to generate tailored product copy.)*"
    )
