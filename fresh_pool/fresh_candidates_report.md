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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=222ms, nekobox=229ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-67MS` (url=216ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=224ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=236ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=223ms, nekobox=226ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=307ms, nekobox=387ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=209ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-240MS` (url=512ms, nekobox=556ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-194MS` (url=2270ms, nekobox=390ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-279MS` (url=2416ms, nekobox=321ms, status=no)
11. `AKUN-009-UNKNOWN-VLESS-WS-263MS`
12. `AKUN-010-WPENG-VLESS-WS-266MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-104MS` (url=201ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-275MS` (url=559ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-374MS` (url=563ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-418MS` (url=967ms, status=HTTP 204)
17. `AKUN-022-CLOUDFLARE-VLESS-WS-384MS` (url=566ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-379MS` (url=744ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-89MS` (url=238ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-521MS` (url=851ms, status=HTTP 204)
21. `AKUN-030-CLOUDFLARE-VLESS-WS-443MS` (url=604ms, status=HTTP 204)
22. `AKUN-031-APPLEID45-VLESS-WS-555MS` (url=1085ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-272MS` (url=514ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-269MS` (url=559ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-627MS` (url=1642ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
