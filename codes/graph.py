import matplotlib.pyplot as plt
import cv2


def plot_result(
    raw_image,
    masked_image,
    result_image,
    title1="Raw Image",
    title2="Masked Image",
    title3="Result Image",
):
    """Plot the raw image, masked image, and the result image side by side."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB))
    axes[0].set_title(title1)
    axes[0].axis("off")

    axes[1].imshow(masked_image, cmap="gray")
    axes[1].set_title(title2)
    axes[1].axis("off")

    axes[2].imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    axes[2].set_title(title3)
    axes[2].axis("off")

    plt.tight_layout()
    plt.show()
