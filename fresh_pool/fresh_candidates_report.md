# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-73MS` (url=225ms, nekobox=245ms, status=yes)
3. `AKUN-003-MYBB-VLESS-WS-79MS` (url=198ms, nekobox=240ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-78MS` (url=202ms, nekobox=305ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=208ms, nekobox=250ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=207ms, nekobox=230ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-98MS` (url=199ms, nekobox=181ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-106MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=194ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-DIGITALOCEAN-VLESS-WS-124MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-108MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-US-VLESS-WS-135MS` (url=197ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-147MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-163MS` (url=843ms, status=HTTP 204)
19. `AKUN-019-CLOUDWEBMANAGE-EU-FR-VLESS-WS-142MS` (url=203ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-76MS` (url=225ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-112MS` (url=313ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-250MS` (url=483ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-260MS` (url=555ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-252MS` (url=558ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-277MS` (url=553ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
