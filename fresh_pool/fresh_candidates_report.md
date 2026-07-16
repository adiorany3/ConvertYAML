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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=390ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=240ms, nekobox=273ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-78MS` (url=295ms, nekobox=289ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=244ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=244ms, nekobox=270ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-87MS` (url=266ms, nekobox=297ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=231ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS` (url=230ms, nekobox=271ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=248ms, nekobox=265ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=269ms, nekobox=254ms, status=yes)
11. `AKUN-011-DEV-VLESS-WS-77MS` (url=248ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-82MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-87MS` (url=276ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-89MS` (url=248ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-98MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-84MS` (url=262ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-124MS` (url=263ms, status=HTTP 204)
18. `AKUN-018-US-VLESS-WS-110MS` (url=251ms, status=HTTP 204)
19. `AKUN-019-NEXUSMODS-VLESS-WS-130MS` (url=270ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-98MS` (url=255ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-106MS` (url=257ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-89MS` (url=235ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-96MS` (url=314ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-123MS` (url=281ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-86MS` (url=256ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
