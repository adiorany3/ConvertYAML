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
1. `AKUN-001-ZVC-VLESS-WS-76MS` (url=369ms, nekobox=355ms, status=yes)
2. `AKUN-002-GOOGLE-VLESS-WS-84MS` (url=409ms, nekobox=377ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-96MS` (url=285ms, nekobox=355ms, status=yes)
4. `AKUN-004-3666888-VLESS-WS-97MS` (url=369ms, nekobox=393ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-105MS` (url=312ms, nekobox=324ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-91MS` (url=376ms, nekobox=353ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-140MS` (url=288ms, nekobox=398ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS` (url=350ms, nekobox=200ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS` (url=415ms, nekobox=245ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=323ms, nekobox=197ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-161MS` (url=286ms, nekobox=207ms, status=no)
12. `AKUN-008-CLOUDFLARE-VLESS-WS-122MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-151MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-184MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-152MS` (url=306ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-168MS` (url=370ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-161MS` (url=347ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-310MS` (url=671ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-202MS` (url=349ms, status=HTTP 204)
20. `AKUN-021-SKK-VLESS-WS-281MS` (url=499ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-354MS` (url=709ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-564MS` (url=2276ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-562MS` (url=1068ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-574MS` (url=1216ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-602MS` (url=1319ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
