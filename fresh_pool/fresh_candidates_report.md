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
1. `AKUN-001-ZVC-VLESS-WS-65MS` (url=221ms, nekobox=224ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-63MS` (url=219ms, nekobox=240ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-60MS` (url=210ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=205ms, nekobox=266ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=202ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-70MS` (url=197ms, nekobox=242ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-73MS` (url=211ms, nekobox=231ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-70MS` (url=211ms, nekobox=228ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-70MS` (url=208ms, nekobox=231ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=201ms, nekobox=233ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=272ms, status=HTTP 204)
12. `AKUN-012-DIGITALOCEAN-VLESS-WS-95MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-99MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-67MS` (url=198ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-84MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-95MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-128MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-118MS` (url=252ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-70MS` (url=256ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-132MS` (url=204ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-138MS` (url=237ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-131MS` (url=243ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-173MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-192MS` (url=247ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-230MS` (url=497ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
