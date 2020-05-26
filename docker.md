# Docker How To

* build the image (first time only)
* run the image


## TODO

Need a way to get a license key in (env var?)


## Build the image
```
docker build . -t deloresdev:latest
```

## Run 'slice_psd' on Source/Rooms/Bank.psd, dumping into MyOutputFolder

```
docker run --rm -it --volume D:\projects\DeloresDev:/delores deloresdev:latest Bin/slice_psd.py Source/Rooms/Bank.psd --images MyOutputFolder
```

## Run 'munge_psd' 
```
docker run --rm -it --volume D:\projects\DeloresDev:/delores deloresdev:latest Bin/munge_psd.py
```

## Run 'munge_images'
```
docker run --rm -it --volume D:\projects\DeloresDev:/delores deloresdev:latest Bin/munge_images.py
```

## Run 'new room'
```
docker run --rm -it --volume D:\projects\DeloresDev:/delores deloresdev:latest Bin/new_room.py MyRoomName
```