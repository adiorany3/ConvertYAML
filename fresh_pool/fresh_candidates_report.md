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
1. `AKUN-001-VULTR-VLESS-WS-82MS` (url=201ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=236ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=232ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-98MS` (url=214ms, nekobox=269ms, status=yes)
5. `AKUN-005-DIGITALOCEAN-VLESS-WS-104MS` (url=240ms, nekobox=434ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=218ms, nekobox=252ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-104MS` (url=234ms, nekobox=260ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS` (url=253ms, nekobox=236ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-103MS` (url=241ms, nekobox=231ms, status=yes)
10. `AKUN-010-WEYRO-NET-VLESS-WS-121MS` (url=254ms, nekobox=252ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-92MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-PAGES-VLESS-WS-112MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-136MS` (url=235ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-106MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-116MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-111MS` (url=205ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-140MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-178MS` (url=610ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-262MS` (url=586ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-263MS` (url=511ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-262MS` (url=562ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-239MS` (url=601ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-250MS` (url=522ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-267MS` (url=606ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-290MS` (url=4968ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
