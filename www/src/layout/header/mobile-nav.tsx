import React from 'react'
import {
  CloseButton,
  VStack,
  useDisclosure,
  useColorModeValue,
  Box,
  IconButton,
  chakra,
  Button
} from '@chakra-ui/react'
import { AiOutlineMenu } from 'react-icons/ai'
import Link from 'next/link'

export default function MobileNav() {
  const mobileNav = useDisclosure()
  return (
    <Box display={{ base: 'inline-flex', md: 'none' }}>
      <IconButton
        display={{ base: 'flex', md: 'none' }}
        aria-label="Open menu"
        fontSize="20px"
        boxShadow={'none'}
        bg={useColorModeValue('gray.50', '#464460')}
        _hover={{ bg: useColorModeValue('gray.50', '#464460') }}
        color={useColorModeValue('gray.800', 'white')}
        onClick={mobileNav.onOpen}
        icon={<AiOutlineMenu />}
      />
      <VStack
        pos="absolute"
        top={0}
        left={0}
        right={0}
        display={mobileNav.isOpen ? 'flex' : 'none'}
        flexDirection="column"
        p={2}
        pb={4}
        m={2}
        bg={useColorModeValue('white', '#1a202cd1')}
        spacing={3}
        rounded="sm"
        shadow="sm"
      >
        <CloseButton aria-label="Close menu" onClick={mobileNav.onClose} />
        <Button as={Link} href={'/browse'} w={'full'} variant={'ghost'}>
          browse
        </Button>
        <Button as={Link} href={'/search'} w={'full'} variant={'ghost'}>
          search
        </Button>
      </VStack>
    </Box>
  )
}
