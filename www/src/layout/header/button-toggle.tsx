import { IconButton, Tooltip, useColorMode } from '@chakra-ui/react'
import { RiMoonFill, RiSunLine } from 'react-icons/ri'

const ThemeToggle = () => {
  const { colorMode, toggleColorMode } = useColorMode()
  return (
    <Tooltip closeOnScroll label="Ativar/desativar tema escuro" placement="bottom-start">
      <IconButton
        aria-label="theme toggle"
        icon={colorMode === 'light' ? <RiMoonFill /> : <RiSunLine />}
        onClick={toggleColorMode}
      />
    </Tooltip>
  )
}

export default ThemeToggle
