# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS` (url=207ms, nekobox=269ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=208ms, nekobox=256ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-81MS` (url=225ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=207ms, nekobox=264ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=207ms, nekobox=249ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-74MS` (url=242ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-120MS` (url=202ms, nekobox=270ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-134MS` (url=231ms, nekobox=239ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-113MS` (url=265ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-149MS` (url=236ms, nekobox=278ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-400MS` (url=805ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-402MS` (url=888ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-342MS` (url=777ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-408MS` (url=2878ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-414MS` (url=819ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-432MS` (url=2855ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-412MS` (url=887ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-644MS` (url=1046ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-655MS` (url=873ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-647MS` (url=934ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-715MS` (url=1064ms, status=HTTP 204)
22. `AKUN-030-CLOUDFLARE-VLESS-WS-790MS` (url=735ms, status=HTTP 204)
23. `AKUN-032-RS-RAPIDSEEDBOX-20190717-VLESS-WS-769MS` (url=1393ms, status=HTTP 204)
24. `AKUN-033-RS-RAPIDSEEDBOX-20190717-VLESS-WS-810MS` (url=1609ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
