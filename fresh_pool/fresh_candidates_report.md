# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 18
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

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
1. `AKUN-001-NEXUSMODS-VLESS-WS-65MS` (url=196ms, nekobox=227ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS` (url=219ms, nekobox=223ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=227ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS` (url=215ms, nekobox=227ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-92MS` (url=199ms, nekobox=245ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=210ms, nekobox=227ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS` (url=195ms, nekobox=221ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-137MS` (url=226ms, nekobox=246ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS` (url=203ms, nekobox=241ms, status=yes)
10. `AKUN-010-BROADNNET-KR-VLESS-WS-87MS` (url=194ms, nekobox=242ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-377MS` (url=758ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-390MS` (url=852ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-404MS` (url=893ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-408MS` (url=865ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-384MS` (url=791ms, status=HTTP 204)
16. `AKUN-017-SPEEDTEST-VLESS-WS-374MS` (url=816ms, status=HTTP 204)
17. `AKUN-029-UNKNOWN-VLESS-WS-729MS` (url=1048ms, status=HTTP 204)
18. `AKUN-034-RS-RAPIDSEEDBOX-20190717-VLESS-WS-879MS` (url=1406ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
