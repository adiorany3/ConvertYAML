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
1. `AKUN-001-ALIBABA-VLESS-WS-75MS` (url=245ms, nekobox=268ms, status=yes)
2. `AKUN-002-ALIBABA-VLESS-WS-73MS` (url=233ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=252ms, nekobox=176ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-102MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-112MS`
6. `AKUN-005-ZOOM-VLESS-WS-94MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-75MS`
8. `AKUN-007-DEV-VLESS-WS-102MS`
9. `AKUN-008-DEV-VLESS-WS-110MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-75MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-75MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=351ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-214MS` (url=395ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-272MS` (url=539ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-258MS` (url=601ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-258MS` (url=548ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=357ms, status=HTTP 204)
19. `AKUN-019-SKK-VLESS-WS-233MS` (url=754ms, status=HTTP 204)
20. `AKUN-020-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-73MS` (url=226ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-414MS` (url=540ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-69MS` (url=224ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-549MS` (url=1390ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-528MS` (url=539ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-563MS` (url=1081ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
