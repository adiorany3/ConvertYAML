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
1. `AKUN-001-VULTR-VLESS-WS-65MS` (url=273ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=265ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=273ms, nekobox=298ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=269ms, nekobox=294ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=268ms, nekobox=321ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=287ms, nekobox=317ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS` (url=293ms, nekobox=196ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-106MS` (url=286ms, nekobox=7180ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-94MS`
11. `AKUN-011-UNKNOWN-VLESS-WS-105MS` (url=290ms, nekobox=177ms, status=no)
12. `AKUN-009-UNKNOWN-VLESS-WS-94MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-86MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-81MS` (url=274ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-115MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-287MS` (url=677ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-118MS` (url=270ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-304MS` (url=664ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-301MS` (url=678ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-300MS` (url=611ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-74MS` (url=273ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-311MS` (url=617ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-263MS` (url=658ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-284MS` (url=546ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-569MS` (url=889ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
