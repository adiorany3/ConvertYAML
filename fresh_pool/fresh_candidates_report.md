# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-UNKNOWN-VLESS-WS-136MS` (url=284ms, nekobox=317ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-133MS` (url=276ms, nekobox=317ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-129MS` (url=273ms, nekobox=307ms, status=yes)
4. `AKUN-004-VULTR-VLESS-WS-161MS` (url=292ms, nekobox=310ms, status=yes)
5. `AKUN-005-DIGITALOCEAN-VLESS-WS-143MS` (url=242ms, nekobox=240ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-163MS`
7. `AKUN-006-ALIBABA-VLESS-WS-165MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-172MS`
9. `AKUN-008-BROADNNET-KR-VLESS-WS-156MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-147MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-370MS`
12. `AKUN-013-UNKNOWN-VLESS-WS-397MS` (url=831ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-389MS` (url=789ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-397MS` (url=791ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-408MS` (url=778ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-404MS` (url=711ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-391MS` (url=749ms, status=HTTP 204)
18. `AKUN-027-RS-RAPIDSEEDBOX-20190717-VLESS-WS-713MS` (url=1202ms, status=HTTP 204)
19. `AKUN-028-CLOUDFLARE-VLESS-WS-657MS` (url=1897ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
