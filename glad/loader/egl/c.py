from glad.loader import BaseLoader

_EGL_LOADER = '''
void gladLoadEGL(void) {
    gladLoadEGLLoader((GLADloadproc)eglGetProcAddress);
}
'''

_EGL_HEADER = '''
#ifndef __glad_egl_h_

#ifdef __egl_h_
#error EGL header already included, remove this include, glad already provides it
#endif

#define __glad_egl_h_
#define __egl_h_

#if defined(_WIN32) && !defined(APIENTRY) && !defined(__CYGWIN__) && !defined(__SCITECH_SNAP__)
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN 1
#endif
#include <windows.h>
#endif

#ifndef APIENTRY
#define APIENTRY
#endif
#ifndef APIENTRYP
#define APIENTRYP APIENTRY *
#endif
#ifndef GLAPI
#define GLAPI extern
#endif

#ifdef __cplusplus
extern "C" {
#endif

typedef void* (* GLADloadproc)(const char *name);
void gladLoadEGLLoader(GLADloadproc);
'''

_EGL_HEADER_LOADER = '''
void gladLoadEGL(void);
'''

_EGL_HEADER_END = '''
#ifdef __cplusplus
}
#endif

#endif
'''

_EGL_HAS_EXT = '''
static int has_ext(const char *ext) {
    return 1;
}
'''


class EGLCLoader(BaseLoader):
    def write(self, fobj, apis):
        if not self.disabled:
            fobj.write(_EGL_LOADER)

    def write_begin_load(self, fobj):
        pass

    def write_find_core(self, fobj):
        pass

    def write_has_ext(self, fobj):
        fobj.write(_EGL_HAS_EXT)

    def write_header(self, fobj):
        fobj.write(_EGL_HEADER)
        if not self.disabled:
            fobj.write(_EGL_HEADER_LOADER)

    def write_header_end(self, fobj):
        fobj.write(_EGL_HEADER_END)

