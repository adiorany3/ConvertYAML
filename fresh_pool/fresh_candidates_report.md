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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=199ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=225ms, nekobox=1030ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-69MS` (url=207ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=205ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=213ms, nekobox=235ms, status=yes)
6. `AKUN-006-VULTR-VLESS-WS-70MS` (url=198ms, nekobox=231ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS` (url=223ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=225ms, nekobox=229ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=209ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-67MS` (url=217ms, nekobox=227ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-119MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-83MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-71MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-142MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-167MS` (url=262ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-132MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-99MS` (url=1667ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-234MS` (url=512ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-132MS` (url=205ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-251MS` (url=2863ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-65MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-269MS` (url=357ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-234MS` (url=539ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-386MS` (url=741ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
