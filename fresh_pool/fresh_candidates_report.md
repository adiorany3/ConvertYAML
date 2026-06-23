# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=209ms, nekobox=243ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-104MS` (url=308ms, nekobox=245ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS` (url=210ms, nekobox=230ms, status=yes)
4. `AKUN-004-DIGITALOCEAN-VLESS-WS-114MS` (url=232ms, nekobox=222ms, status=no)
5. `AKUN-004-ALIBABA-VLESS-WS-83MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS`
8. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-102MS`
9. `AKUN-008-BROADNNET-KR-VLESS-WS-133MS`
10. `AKUN-009-BROADNNET-KR-VLESS-WS-112MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-251MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-282MS` (url=566ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-277MS` (url=583ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-291MS` (url=552ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-291MS` (url=569ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-298MS` (url=574ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-271MS` (url=568ms, status=HTTP 204)
18. `AKUN-030-UNKNOWN-VLESS-WS-496MS` (url=724ms, status=HTTP 204)
19. `AKUN-034-UNKNOWN-VLESS-WS-567MS` (url=4003ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
