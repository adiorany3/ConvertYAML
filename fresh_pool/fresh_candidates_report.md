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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=231ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=228ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=248ms, nekobox=264ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=242ms, nekobox=283ms, status=yes)
5. `AKUN-005-BGP48-HK-VLESS-WS-79MS` (url=262ms, nekobox=299ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-88MS` (url=233ms, nekobox=302ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=249ms, nekobox=263ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-93MS` (url=270ms, nekobox=275ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=233ms, nekobox=276ms, status=yes)
10. `AKUN-010-CZ-LOTUNA-19970206-VLESS-WS-94MS` (url=266ms, nekobox=335ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=251ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=293ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-96MS` (url=257ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=300ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-133MS` (url=299ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-135MS` (url=273ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-137MS` (url=294ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-137MS` (url=259ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-124MS` (url=242ms, status=HTTP 204)
20. `AKUN-020-BGP48-HK-VLESS-WS-153MS` (url=259ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-130MS` (url=275ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-215MS` (url=311ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-283MS` (url=634ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-301MS` (url=651ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-302MS` (url=683ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
