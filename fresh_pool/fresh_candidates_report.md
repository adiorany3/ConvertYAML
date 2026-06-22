# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=207ms, nekobox=267ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-65MS` (url=228ms, nekobox=251ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-63MS` (url=216ms, nekobox=238ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=220ms, nekobox=253ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=221ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=227ms, nekobox=269ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=234ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-130MS` (url=215ms, nekobox=229ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=287ms, nekobox=185ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-165MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=179ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-356MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-384MS` (url=835ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-419MS` (url=846ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-418MS` (url=860ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-427MS` (url=852ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-360MS` (url=773ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-367MS` (url=782ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-702MS` (url=958ms, status=HTTP 204)
20. `AKUN-027-UNKNOWN-VLESS-WS-751MS` (url=1266ms, status=HTTP 204)
21. `AKUN-030-UNKNOWN-VLESS-WS-857MS` (url=1406ms, status=HTTP 204)
22. `AKUN-032-UNKNOWN-VLESS-WS-860MS` (url=1762ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-830MS` (url=1246ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
