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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-ORACLE-VLESS-WS-55MS` (url=208ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-56MS` (url=209ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=209ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-59MS` (url=218ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-60MS` (url=215ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-56MS` (url=212ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-61MS` (url=211ms, nekobox=238ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-68MS` (url=211ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-59MS` (url=211ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS` (url=230ms, nekobox=171ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS`
12. `AKUN-012-DEV-VLESS-WS-60MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-54MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-69MS` (url=1699ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-88MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-62MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-56MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-108MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-59MS` (url=243ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-64MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-324MS` (url=710ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-351MS` (url=868ms, status=HTTP 204)
23. `AKUN-023-NET-141-11-202-0-23-VLESS-WS-361MS` (url=747ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-397MS` (url=1929ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-625MS` (url=974ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
