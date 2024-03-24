# Use Ubuntu Bionic as the base image
FROM ubuntu:bionic

# Set the timezone to UTC
RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime && echo "Etc/UTC" > /etc/timezone

# Update the package lists and install texlive-full
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y texlive-full && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /root/shared_folder

# Define the default command to run when the container starts
CMD ["/bin/bash"]