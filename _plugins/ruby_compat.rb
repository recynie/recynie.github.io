# Compatibility shim for legacy Liquid/Jekyll versions on modern Ruby.
# Ruby 3.2+ removed the taint API, but Liquid 4.0.3 still calls it.
class Object
  unless method_defined?(:tainted?)
    def tainted?
      false
    end
  end

  unless method_defined?(:taint)
    def taint
      self
    end
  end

  unless method_defined?(:untaint)
    def untaint
      self
    end
  end
end

if defined?(Pathutil)
  class Pathutil
    def read(*args, **kwd)
      kwd[:encoding] ||= encoding

      if normalize[:read]
        File.read(self, *args, **kwd).encode(
          universal_newline: true
        )
      else
        File.read(self, *args, **kwd)
      end
    end

    def binread(*args, **kwd)
      kwd[:encoding] ||= encoding

      if normalize[:read]
        File.binread(self, *args, **kwd).encode(
          universal_newline: true
        )
      else
        File.binread(self, *args, **kwd)
      end
    end
  end
end
