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
1. `AKUN-001-UNKNOWN-VLESS-WS-74MS` (url=201ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=216ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=286ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=220ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=221ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=220ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=223ms, nekobox=243ms, status=yes)
8. `AKUN-008-NATO-US-2-VLESS-WS-90MS` (url=209ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=219ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS` (url=233ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-106MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-91MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-133MS` (url=348ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-110MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-76MS` (url=231ms, status=HTTP 204)
16. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-183MS` (url=282ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-180MS` (url=506ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-181MS` (url=310ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-238MS` (url=1970ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-316MS` (url=708ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-410MS` (url=672ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-476MS` (url=1110ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-446MS` (url=732ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-488MS` (url=772ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-516MS` (url=865ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
