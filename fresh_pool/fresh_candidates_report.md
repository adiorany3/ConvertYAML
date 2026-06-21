# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=345ms, nekobox=327ms, status=yes)
2. `AKUN-002-ALIBABA-VLESS-WS-73MS` (url=277ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=266ms, nekobox=312ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=276ms, nekobox=305ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=306ms, nekobox=320ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS` (url=265ms, nekobox=312ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=277ms, nekobox=319ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-91MS` (url=272ms, nekobox=303ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=278ms, nekobox=330ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-92MS` (url=354ms, nekobox=316ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-285MS` (url=721ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-288MS` (url=631ms, status=HTTP 204)
13. `AKUN-013-MICROSOFT-VLESS-WS-301MS` (url=677ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-269MS` (url=557ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-306MS` (url=650ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-265MS` (url=620ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-283MS` (url=568ms, status=HTTP 204)
18. `AKUN-032-UNKNOWN-VLESS-WS-458MS` (url=771ms, status=HTTP 204)
19. `AKUN-033-UNKNOWN-VLESS-WS-657MS` (url=953ms, status=HTTP 204)
20. `AKUN-034-UNKNOWN-VLESS-WS-632MS` (url=4665ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
