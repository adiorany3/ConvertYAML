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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=249ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=236ms, nekobox=288ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-72MS` (url=267ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=253ms, nekobox=294ms, status=yes)
5. `AKUN-005-MYBB-VLESS-WS-75MS` (url=253ms, nekobox=269ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=235ms, nekobox=261ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=232ms, nekobox=337ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=260ms, nekobox=270ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS` (url=275ms, nekobox=304ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=239ms, nekobox=271ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=248ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-123MS` (url=260ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-112MS` (url=240ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-93MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-ADF-VLESS-WS-71MS` (url=266ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-82MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=235ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-257MS` (url=551ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-266MS` (url=584ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-299MS` (url=668ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-293MS` (url=495ms, status=HTTP 204)
23. `AKUN-024-SPEEDTEST-VLESS-WS-305MS` (url=639ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-299MS` (url=681ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-311MS` (url=622ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
