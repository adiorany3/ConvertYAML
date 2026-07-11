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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=240ms, nekobox=257ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=251ms, nekobox=274ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=231ms, nekobox=269ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-71MS` (url=241ms, nekobox=261ms, status=yes)
5. `AKUN-005-NET-82-21-84-0-24-VLESS-WS-85MS` (url=282ms, nekobox=356ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-84MS` (url=237ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=241ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=245ms, nekobox=277ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=253ms, nekobox=189ms, status=no)
10. `AKUN-009-UNKNOWN-VLESS-WS-71MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS`
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-79MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-86MS` (url=249ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-104MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-109MS` (url=254ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-107MS` (url=261ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-121MS` (url=246ms, status=HTTP 204)
18. `AKUN-019-466688-VLESS-WS-132MS` (url=259ms, status=HTTP 204)
19. `AKUN-020-ORG-VLESS-WS-128MS` (url=251ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-261MS` (url=551ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-267MS` (url=569ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-299MS` (url=649ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-310MS` (url=2973ms, status=HTTP 204)
24. `AKUN-025-SPEEDTEST-VLESS-WS-286MS` (url=601ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-78MS` (url=245ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
