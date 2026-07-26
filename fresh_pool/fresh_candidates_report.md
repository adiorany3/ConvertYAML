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
1. `AKUN-001-UNKNOWN-VLESS-WS-54MS` (url=202ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-54MS` (url=222ms, nekobox=229ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-55MS` (url=201ms, nekobox=231ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-57MS` (url=202ms, nekobox=234ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-57MS` (url=202ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-55MS` (url=209ms, nekobox=240ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-64MS` (url=213ms, nekobox=247ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-56MS` (url=203ms, nekobox=339ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-76MS` (url=208ms, nekobox=231ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-69MS` (url=222ms, nekobox=173ms, status=no)
11. `AKUN-010-ZOOM-VLESS-WS-74MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-57MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-SKK-VLESS-WS-84MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-65MS` (url=201ms, status=HTTP 204)
16. `AKUN-016-008500-VLESS-WS-77MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-60MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-95MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-65MS` (url=210ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-56MS` (url=211ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-116MS` (url=213ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-95MS` (url=212ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-334MS` (url=764ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-324MS` (url=2825ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-339MS` (url=722ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
