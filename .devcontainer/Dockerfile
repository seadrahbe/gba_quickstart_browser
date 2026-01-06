FROM devkitpro/devkitarm:latest

# Install xpra for x forwarding GUI apps like libresprite
# Install supervisor to nanny xpra and the emulator webserver
# Get xpra key
RUN wget -O /usr/share/keyrings/xpra.asc https://xpra.org/xpra.asc && \
    wget -O /etc/apt/sources.list.d/xpra-lts.sources \
    https://raw.githubusercontent.com/Xpra-org/xpra/master/packaging/repos/bookworm/xpra-lts.sources && \
    apt-get update && \
    apt-get install -y xpra supervisor && \
    rm -rf /var/lib/apt/lists/*


ARG LIBRESPRITE_VERSION=1.2
ARG LIBRESPRITE_APPIMAGE=LibreSprite-anylinux-x86_64.AppImage
ARG LIBRESPRITE_URL=https://github.com/LibreSprite/LibreSprite/releases/download/v${LIBRESPRITE_VERSION}/${LIBRESPRITE_APPIMAGE}

# Make /tools and download LibreSprite AppImage
# Extract the AppImage to work around lack of FUSE support
RUN mkdir -p /tools
WORKDIR /tools
RUN curl -fL "${LIBRESPRITE_URL}" -o ${LIBRESPRITE_APPIMAGE} && \
    chmod +x ${LIBRESPRITE_APPIMAGE} && \
    ./${LIBRESPRITE_APPIMAGE} --appimage-extract && \
    mv squashfs-root libresprite && \
    rm ${LIBRESPRITE_APPIMAGE}

# Set up libresprite so it scales properly in xpra
RUN mkdir -p /root/.config/libresprite
COPY config/libresprite.ini /root/.config/libresprite/libresprite.ini

# Copy configration for supervised processes (currently LibreSprite and emulator)
COPY config/supervisor/ /etc/supervisor/conf.d/

# Copy devcontainer and process scripts.
# By default devoncontainer.json reads from the image copy, NOT the one in the clone of the repo
# This means that when there are image updates, you can get the new functionality just by recreating
# your Codespace. You don't need to pull in any changes.
COPY scripts/ /scripts

# Copy the Python and static assets for the emulation tool
COPY emuserver/ /emuserver

CMD [ "bash" ]