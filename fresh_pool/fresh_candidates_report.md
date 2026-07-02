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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=234ms, nekobox=261ms, status=yes)
2. `AKUN-002-UK-GB-DCL-01-20191003-VLESS-WS-81MS` (url=273ms, nekobox=264ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-86MS` (url=260ms, nekobox=274ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=258ms, nekobox=273ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=299ms, nekobox=288ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-82MS` (url=254ms, nekobox=312ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=374ms, nekobox=294ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-96MS` (url=239ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=243ms, nekobox=284ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-94MS` (url=277ms, nekobox=386ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-80MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-104MS` (url=269ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-101MS` (url=242ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-108MS` (url=260ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-109MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-121MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-119MS` (url=268ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-79MS` (url=278ms, status=HTTP 204)
19. `AKUN-019-WEBEX-VLESS-WS-138MS` (url=272ms, status=HTTP 204)
20. `AKUN-020-PAGES-VLESS-WS-136MS` (url=280ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-265MS` (url=554ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-281MS` (url=599ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-279MS` (url=623ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-116MS` (url=287ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-288MS` (url=608ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
