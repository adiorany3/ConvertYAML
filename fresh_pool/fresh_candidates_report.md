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
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-877774-VLESS-WS-81MS` (url=236ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=233ms, nekobox=198ms, status=no)
3. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-82MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-112MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-111MS`
7. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-92MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-177MS` (url=344ms, nekobox=302ms, status=no)
10. `AKUN-008-UNKNOWN-VLESS-WS-198MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-251MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-185MS` (url=5656ms, nekobox=426ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-289MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-286MS` (url=3322ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-280MS` (url=612ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-279MS` (url=599ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-299MS` (url=613ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-461MS` (url=732ms, status=HTTP 204)
19. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-496MS` (url=840ms, status=HTTP 204)
20. `AKUN-029-UNKNOWN-VLESS-WS-529MS` (url=858ms, status=HTTP 204)
21. `AKUN-033-CLOUDFLARE-VLESS-WS-702MS` (url=1687ms, status=HTTP 204)
22. `AKUN-034-UNKNOWN-VLESS-WS-239MS` (url=1065ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
