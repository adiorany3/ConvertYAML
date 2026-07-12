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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=239ms, nekobox=256ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-72MS` (url=231ms, nekobox=268ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-66MS` (url=225ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=219ms, nekobox=266ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=258ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-77MS` (url=219ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=218ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=239ms, nekobox=251ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=236ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=217ms, nekobox=244ms, status=yes)
11. `AKUN-011-PUBLICDOMAINREGISTRY-NET-VLESS-WS-124MS` (url=259ms, status=HTTP 204)
12. `AKUN-012-HETZNER-VLESS-WS-117MS` (url=235ms, status=HTTP 204)
13. `AKUN-013-HGC-GLOBAL-COMMUNICATION-VLESS-WS-120MS` (url=239ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-126MS` (url=240ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-64MS` (url=238ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=219ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-105MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-343MS` (url=756ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-388MS` (url=864ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-375MS` (url=912ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-244MS` (url=435ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-570MS` (url=915ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-67MS` (url=795ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-673MS` (url=1018ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-707MS` (url=1136ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
