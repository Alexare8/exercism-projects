class LogLineParser
    attr_accessor :message, :log_level
  
  def initialize(line)
    @message = line[line.index(":") + 1..].strip
    @log_level = line[1..line.index("]") - 1].downcase
  end

  def reformat
    "#{message} (#{log_level})"
  end
end
