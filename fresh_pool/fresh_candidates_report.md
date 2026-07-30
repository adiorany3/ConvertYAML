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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=211ms, nekobox=222ms, status=yes)
2. `AKUN-002-FMN5-RENTED-NET2-VLESS-WS-64MS` (url=218ms, nekobox=242ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-62MS` (url=198ms, nekobox=253ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-78MS` (url=208ms, nekobox=241ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-77MS` (url=215ms, nekobox=229ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=200ms, nekobox=227ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS` (url=197ms, nekobox=229ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=216ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-67MS` (url=209ms, nekobox=232ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-84MS` (url=214ms, nekobox=224ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-101MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-72MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-877774-VLESS-WS-76MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-108MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-125MS` (url=341ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-107MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-109MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-96MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-99MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-221MS` (url=494ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-172MS` (url=278ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-178MS` (url=347ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-300MS` (url=713ms, status=HTTP 204)
24. `AKUN-025-TIME-VLESS-WS-351MS` (url=376ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-388MS` (url=650ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
