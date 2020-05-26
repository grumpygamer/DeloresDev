FROM python:2

WORKDIR /delores

RUN apt-get update && \
	apt-get install -y make libgl1-mesa-glx  libglib2.0-0 wget npm git dpkg && \
	rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip psd-tools pillow

RUN wget "https://www.codeandweb.com/download/texturepacker/5.3.0/TexturePacker-5.3.0-ubuntu64.deb" -O TexturePacker.deb
RUN /usr/bin/dpkg -i TexturePacker.deb
RUN echo agree | TexturePacker --version

ENV DELORES_GAMEROOT /delores
ENV TEXTURE_PACKER_CMD /usr/bin/TexturePacker
			
ENTRYPOINT ["python"]
CMD []
