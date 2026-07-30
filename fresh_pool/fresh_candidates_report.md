# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-SEECK-VLESS-WS-56MS` (url=214ms, nekobox=230ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-57MS` (url=203ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=220ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS`
6. `AKUN-006-UNKNOWN-VLESS-WS-65MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS`
8. `AKUN-008-UNKNOWN-VLESS-WS-64MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=232ms, status=HTTP 204)
12. `AKUN-014-PAGES-VLESS-WS-132MS` (url=229ms, status=HTTP 204)
13. `AKUN-015-NET-USA-VLESS-WS-83MS` (url=206ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-329MS` (url=1350ms, status=HTTP 204)
15. `AKUN-021-TW-CLOUD-VLESS-WS-427MS` (url=981ms, status=HTTP 204)
16. `AKUN-022-CLOUDFLARE-VLESS-WS-362MS` (url=660ms, status=HTTP 204)
17. `AKUN-023-CLOUDFLARE-VLESS-WS-456MS` (url=980ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-607MS` (url=963ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-675MS` (url=1196ms, status=HTTP 204)
20. `AKUN-033-CLOUDFLARE-VLESS-WS-802MS` (url=1321ms, status=HTTP 204)
21. `AKUN-034-UNKNOWN-VLESS-WS-815MS` (url=2367ms, status=HTTP 204)
22. `AKUN-035-CLOUDFLARE-VLESS-WS-888MS` (url=1249ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
