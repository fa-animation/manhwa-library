import React from 'react'
import {
  chakra,
  Flex,
  HStack,
  VisuallyHidden,
  useColorModeValue,
  ButtonGroup
} from '@chakra-ui/react'
import NextLink from 'next/link'
import ThemeToggle from './button-toggle'

type HeaderProps = {
  children: React.ReactNode
}

const Header = ({ children }: HeaderProps) => (
  <chakra.header
    borderTop="5px solid #4299e1"
    shadow="md"
    transition="all 0.5s ease-in-out"
    pos="fixed"
    top="0"
    zIndex="modal"
    w="full"
    px={{ base: 2, sm: 4 }}
    py={4}
    mb={10}
    css={{
      backdropFilter: 'saturate(180%) blur(5px)',
      backgroundColor: useColorModeValue('rgba(255, 255, 255, 0.8)', 'rgba(26, 32, 44, 0.8)')
    }}
  >
    {children}
  </chakra.header>
)

export default function NavHero() {
  return (
    <Header>
      <Flex alignItems="center" justifyContent="space-between" mx="auto" as="nav">
        <Flex>
          <VisuallyHidden>Logo</VisuallyHidden>
          <NextLink href={'/'}>
            <chakra.h1 fontSize="xl" fontWeight="medium" ml="2">
              Manhwa Library
            </chakra.h1>
          </NextLink>
        </Flex>
        <HStack display="flex" alignItems="center" spacing={1}>
          {/* <DesktopNav /> */}
          <ButtonGroup>
            <ThemeToggle />
          </ButtonGroup>
          {/* <MobileNav /> */}
        </HStack>
      </Flex>
    </Header>
  )
}
