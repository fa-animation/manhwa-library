import { Box, Image, Skeleton, Text } from '@chakra-ui/react'
import Link from 'next/link'

type PosterCardProps = {
  name?: string
  imageUrl?: string
  slug: string
}

const PosterCard = ({ name, imageUrl, slug }: PosterCardProps) => {
  return (
    <Link href={`/manga/${slug}`}>
      <Box as="button" borderRadius={24} _groupHover={{ backgroundColor: 'black' }}>
        <Image
          _groupHover={{ opacity: 0.3 }}
          borderRadius={24}
          src={imageUrl}
          style={{
            height: '15rem',
            width: '13em'
          }}
          alt={name}
          fallback={<Skeleton />}
        />
      </Box>
      <Text
        textTransform="uppercase"
        fontSize="xs"
        letterSpacing={2}
        textAlign="center"
        position="absolute"
        top="50%"
        left="50%"
        transform="translate(-50%, -50%)"
        visibility="hidden"
        color="white"
        _groupHover={{ visibility: 'visible' }}
        fontWeight={'bold'}
      >
        {name}
      </Text>
    </Link>
  )
}

export default PosterCard
