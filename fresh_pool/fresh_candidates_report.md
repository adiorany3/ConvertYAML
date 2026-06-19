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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=207ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=206ms, nekobox=235ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-75MS` (url=230ms, nekobox=258ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-105MS` (url=228ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS` (url=229ms, nekobox=235ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=231ms, nekobox=238ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=226ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS` (url=235ms, nekobox=234ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-246MS` (url=528ms, nekobox=588ms, status=yes)
10. `AKUN-010-CONFLU-VLESS-WS-255MS` (url=522ms, nekobox=570ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-269MS` (url=588ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-282MS` (url=569ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-290MS` (url=2114ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-282MS` (url=576ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-313MS` (url=2364ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-273MS` (url=580ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-416MS` (url=571ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-395MS` (url=683ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-464MS` (url=824ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-418MS` (url=607ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-467MS` (url=587ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-423MS` (url=668ms, status=HTTP 204)
23. `AKUN-029-UNKNOWN-VLESS-WS-499MS` (url=808ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-561MS` (url=880ms, status=HTTP 204)
25. `AKUN-032-APPLEID45-VLESS-WS-574MS` (url=1086ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
