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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=224ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=221ms, nekobox=270ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-60MS` (url=223ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-57MS` (url=220ms, nekobox=266ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-55MS` (url=219ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-60MS` (url=230ms, nekobox=249ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-75MS` (url=246ms, nekobox=269ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-73MS` (url=228ms, nekobox=257ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-63MS` (url=255ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-58MS` (url=221ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-81MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-66MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-101MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-55MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-61MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-133MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-92MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-143MS` (url=235ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-253MS` (url=572ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-256MS` (url=584ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-272MS` (url=846ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-416MS` (url=705ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-449MS` (url=986ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
