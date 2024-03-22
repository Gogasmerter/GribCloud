import Body from '@/components/Body/Body'
import ImagesRender from '@/components/ImagesRednder/ImagesRender'
import ModalImageEdit from '@/components/Modal/ModalImageEdit'
import ModalMap from '@/components/Modal/ModalMap'
import useAlbums from '@/hooks/useAlbums'
import { useFiles } from '@/hooks/useFiles'
import { AlbumResponse, UploadImageResponse } from '@/redux/types'
import { useDisclosure } from '@mantine/hooks'
import { FunctionComponent, useEffect, useState } from 'react'

interface AlbumProps {
  currentAlbum: AlbumResponse
}

const Album: FunctionComponent<AlbumProps> = ({ currentAlbum }) => {
  const { loading, uploadedImages, setFiles } = useFiles(
    window.location.href.split('/'),
    currentAlbum.title,
  )
  const [url, setUrl] = useState<string | undefined>(undefined)
  const [name, setName] = useState<string | undefined>(undefined)
  const [opened, { open, close }] = useDisclosure(false)
  const [openedMap, { open: openMap, close: closeMap }] = useDisclosure(false)
  const [latitude, setLatitude] = useState<number | undefined>(undefined)
  const [longitude, setLongitude] = useState<number | undefined>(undefined)
  const [key, setKey] = useState(0)
  const [tagKey, setTagKey] = useState(0)
  const { removeImageFromAlbum, albumLoading } = useAlbums()
  const [userImages, setUserImages] = useState<UploadImageResponse[]>([])

  const handleRemoveImageFromAlbum = async (
    album: AlbumResponse,
    image: number,
    path: string,
  ) => {
    await removeImageFromAlbum(album, image, path)
    setUserImages(prevImages => prevImages.filter(img => img.id !== image))
  }
  const allLoading = loading || albumLoading
  useEffect(() => {
    if (uploadedImages) {
      setUserImages(uploadedImages)
    }
  }, [uploadedImages])
  return (
    <Body key={key} loading={allLoading}>
      <ImagesRender
        setTagKey={setTagKey}
        tagKey={tagKey}
        handleRemoveImageFromAlbum={handleRemoveImageFromAlbum}
        album={currentAlbum}
        openMap={openMap}
        setLatitude={setLatitude}
        setLongitude={setLongitude}
        open={open}
        setName={setName}
        setFiles={setFiles}
        setUrl={setUrl}
        userImages={userImages}
      />
      {url && name && (
        <ModalImageEdit
          setKey={setKey}
          opened={opened}
          close={close}
          url={url}
          name={name}
        />
      )}
      {latitude && longitude && (
        <ModalMap
          openedMap={openedMap}
          closeMap={closeMap}
          latitude={latitude}
          longitude={longitude}
        />
      )}
    </Body>
  )
}

export default Album
