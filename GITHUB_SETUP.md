# Publishing CleanSweep to GitHub

Since the GitHub CLI (`gh`) is not installed, you'll need to create the repository manually on GitHub.

## 1. Create the Repository

1.  Go to **[github.com/new](https://github.com/new)**.
2.  **Repository name**: `CleanSweep`
3.  **Description**: 
    > CleanSweep 🧹: An intelligent, real-time desktop file organizer powered by Python and Watchdog.
4.  **Visibility**: Choose **Public** or **Private**.
5.  **Initialize this repository with**: Leave all unchecked (we already have code).
6.  Click **Create repository**.

## 2. Push Your Code

Copy the commands under "**…or push an existing repository from the command line**" from the GitHub page. They will look like this (replace `YOUR_USERNAME` with your actual GitHub username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/CleanSweep.git
git branch -M main
git push -u origin main
```

Run these commands in your terminal here.
