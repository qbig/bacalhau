/*
Copyright 2016 The Kubernetes Authors.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package templates

import (
	"strings"

	"github.com/MakeNowJust/heredoc/v2"
	"github.com/russross/blackfriday"
)

const Indentation = `  `

// LongDesc normalizes a command's long description to follow the conventions.
func LongDesc(s string) string {
	if s == "" {
		return s
	}
	return normalizer{s}.heredoc().markdown().trim().string
}

// Examples normalizes a command's examples to follow the conventions.
func Examples(s string) string {
	if s == "" {
		return s
	}
	return normalizer{s}.trim().indent().string
}

type normalizer struct {
	string
}

func (s normalizer) markdown() normalizer {
	bytes := []byte(s.string)
	formatted := blackfriday.Markdown(bytes, &ASCIIRenderer{Indentation: Indentation}, blackfriday.EXTENSION_NO_INTRA_EMPHASIS)
	s.string = string(formatted)
	return s
}

func (s normalizer) heredoc() normalizer {
	s.string = heredoc.Doc(s.string)
	return s
}

func (s normalizer) trim() normalizer {
	s.string = strings.TrimSpace(s.string)
	return s
}

func (s normalizer) indent() normalizer {
	var indentedLines []string
	for _, line := range strings.Split(s.string, "\n") {
		trimmed := strings.TrimSpace(line)
		indented := Indentation + trimmed
		indentedLines = append(indentedLines, indented)
	}
	s.string = strings.Join(indentedLines, "\n")
	return s
}
