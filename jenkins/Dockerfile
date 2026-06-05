# imagem customizada para incluir node e docker cli (imagem oficial não inclui)

FROM jenkins/jenkins:lts-jdk17

ENV CASC_JENKINS_CONFIG="/var/jenkins_home/casc.yaml"

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    python3 \
    ca-certificates \
    gnupg \
    lsb-release \
    gosu \
    xvfb \
    xauth \
    libgtk2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxtst6 \
    libnotify4 \
    && rm -rf /var/lib/apt/lists/*

# instala o node js
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# instala o docker cli
RUN curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) \
        signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
        https://download.docker.com/linux/debian \
        $(lsb_release -cs) stable" \
        > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -f docker && usermod -aG docker jenkins

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

COPY casc.yaml /var/jenkins_home/casc.yaml

EXPOSE 8080 50000

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
