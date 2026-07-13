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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=200ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=202ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=214ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=228ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS` (url=198ms, nekobox=257ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=215ms, nekobox=228ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS` (url=230ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=229ms, nekobox=235ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-63MS` (url=214ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=207ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-77MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-83MS` (url=209ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-102MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-103MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-88MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-NET-82-21-84-0-24-VLESS-WS-127MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-HETZNER-VLESS-WS-87MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-110MS` (url=211ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-133MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-HETZNER-VLESS-WS-103MS` (url=228ms, status=HTTP 204)
21. `AKUN-021-WPENG-VLESS-WS-144MS` (url=221ms, status=HTTP 204)
22. `AKUN-022-INTERNETWORKS-45-131-210-VLESS-WS-233MS` (url=530ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-240MS` (url=484ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-242MS` (url=494ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-270MS` (url=547ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
