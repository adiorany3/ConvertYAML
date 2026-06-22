# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-139MS` (url=283ms, nekobox=324ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-150MS` (url=282ms, nekobox=309ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-137MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-156MS`
5. `AKUN-006-CLOUDFLARE-VLESS-WS-141MS` (url=286ms, nekobox=7176ms, status=no)
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-150MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-156MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-179MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-358MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-380MS`
12. `AKUN-014-CLOUDFLARE-VLESS-WS-404MS` (url=787ms, status=HTTP 204)
13. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-402MS` (url=770ms, status=HTTP 204)
14. `AKUN-019-UNKNOWN-VLESS-WS-441MS` (url=893ms, status=HTTP 204)
15. `AKUN-021-CLOUDFLARE-VLESS-WS-387MS` (url=776ms, status=HTTP 204)
16. `AKUN-022-CLOUDFLARE-VLESS-WS-145MS` (url=339ms, status=HTTP 204)
17. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-650MS` (url=895ms, status=HTTP 204)
18. `AKUN-027-CLOUDFLARE-VLESS-WS-661MS` (url=1047ms, status=HTTP 204)
19. `AKUN-030-CLOUDFLARE-VLESS-WS-779MS` (url=2228ms, status=HTTP 204)
20. `AKUN-031-BROADNNET-KR-VLESS-WS-437MS` (url=797ms, status=HTTP 204)
21. `AKUN-032-CLOUDFLARE-VLESS-WS-810MS` (url=1223ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
