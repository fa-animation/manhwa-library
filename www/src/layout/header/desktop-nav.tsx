import { Button, HStack, chakra } from '@chakra-ui/react'
import Link from 'next/link'

export default function DesktopNav() {
  return (
    <HStack spacing={1} mr={1} color="brand.500" display={{ base: 'none', md: 'inline-flex' }}>
      <Button variant={'ghost'} as={Link} href={'/browse'}>
        browse
      </Button>
      <Button variant={'ghost'} as={Link} href={'/search'}>
        search
      </Button>
    </HStack>
  )
}
